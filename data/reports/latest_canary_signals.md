# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T11:37:32.398432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `0.1126` n `230`; crypto_major avg `0.042` n `8`; equity avg `0.3794` n `109`; fx avg `-0.0021` n `6`; index avg `0.0407` n `25`; metal avg `0.0204` n `20`; unknown avg `0.0353` n `781`
- 1h: commodity avg `-0.0245` n `12`; crypto_alt avg `0.1514` n `230`; crypto_major avg `0.1063` n `8`; equity avg `0.043` n `109`; fx avg `0.0139` n `6`; index avg `-0.006` n `25`; metal avg `-0.0453` n `20`; unknown avg `-0.0152` n `781`
- 4h: commodity avg `0.0048` n `12`; crypto_alt avg `-0.2903` n `230`; crypto_major avg `-0.4403` n `8`; equity avg `-0.0752` n `109`; fx avg `-0.045` n `6`; index avg `-0.0312` n `25`; metal avg `0.1168` n `20`; unknown avg `108.1846` n `781`
- 24h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.1886` n `230`; crypto_major avg `-0.3544` n `8`; equity avg `-1.5676` n `109`; fx avg `-0.0023` n `6`; index avg `-0.3893` n `25`; metal avg `0.2768` n `20`; unknown avg `113.0539` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
