# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T12:07:33.319825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1269` n `12`; crypto_alt avg `-0.041` n `230`; crypto_major avg `-0.0312` n `8`; equity avg `-0.0737` n `107`; fx avg `-0.0449` n `6`; index avg `-0.0364` n `25`; metal avg `-0.0442` n `20`; unknown avg `-0.0063` n `781`
- 1h: commodity avg `-0.6601` n `12`; crypto_alt avg `0.0281` n `230`; crypto_major avg `0.2625` n `8`; equity avg `0.2762` n `107`; fx avg `-0.0871` n `6`; index avg `0.0877` n `25`; metal avg `0.2926` n `20`; unknown avg `0.0423` n `781`
- 4h: commodity avg `-0.777` n `12`; crypto_alt avg `-0.1659` n `230`; crypto_major avg `0.3408` n `8`; equity avg `0.5333` n `107`; fx avg `-0.0994` n `6`; index avg `0.0913` n `25`; metal avg `0.2238` n `20`; unknown avg `0.0698` n `781`
- 24h: commodity avg `-0.4523` n `12`; crypto_alt avg `1.0654` n `230`; crypto_major avg `1.9345` n `8`; equity avg `5.5478` n `107`; fx avg `0.0119` n `6`; index avg `0.6715` n `25`; metal avg `0.6243` n `20`; unknown avg `0.9105` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
