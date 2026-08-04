# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T03:52:39.283430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `0.0743` n `230`; crypto_major avg `0.0505` n `8`; equity avg `0.0617` n `107`; fx avg `-0.0055` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.0537` n `781`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `-0.092` n `230`; crypto_major avg `-0.0494` n `8`; equity avg `0.1428` n `107`; fx avg `0.0264` n `6`; index avg `-0.0186` n `25`; metal avg `-0.0235` n `20`; unknown avg `-0.0059` n `780`
- 4h: commodity avg `0.1626` n `12`; crypto_alt avg `0.2484` n `230`; crypto_major avg `0.3647` n `8`; equity avg `-0.3566` n `107`; fx avg `-0.0036` n `6`; index avg `-0.1164` n `25`; metal avg `0.1727` n `20`; unknown avg `-0.3002` n `780`
- 24h: commodity avg `0.2725` n `12`; crypto_alt avg `1.2895` n `230`; crypto_major avg `1.1391` n `8`; equity avg `1.4981` n `107`; fx avg `0.0296` n `6`; index avg `0.0775` n `25`; metal avg `0.0001` n `20`; unknown avg `0.2503` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
