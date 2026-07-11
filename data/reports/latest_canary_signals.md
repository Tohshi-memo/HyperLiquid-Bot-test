# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T07:52:26.069753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.0082` n `8`; equity avg `-0.0012` n `92`; fx avg `0.0063` n `6`; index avg `0.0011` n `25`; metal avg `-0.0032` n `20`; unknown avg `-0.0233` n `765`
- 1h: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0304` n `230`; crypto_major avg `-0.0151` n `8`; equity avg `-0.0082` n `92`; fx avg `0.0041` n `6`; index avg `0.0187` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0253` n `763`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.2438` n `229`; crypto_major avg `-0.0669` n `8`; equity avg `0.0924` n `92`; fx avg `0.022` n `6`; index avg `0.0139` n `25`; metal avg `-0.019` n `20`; unknown avg `-0.0037` n `733`
- 24h: commodity avg `-0.087` n `12`; crypto_alt avg `0.4026` n `229`; crypto_major avg `-0.0673` n `8`; equity avg `0.1936` n `92`; fx avg `-0.0764` n `6`; index avg `0.1978` n `25`; metal avg `0.0831` n `20`; unknown avg `2.9187` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
