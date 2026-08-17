# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T18:52:34.233653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `0.0241` n `230`; crypto_major avg `-0.0323` n `8`; equity avg `0.0478` n `114`; fx avg `0.0059` n `6`; index avg `0.0071` n `25`; metal avg `0.0333` n `20`; unknown avg `-0.0487` n `792`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `0.1138` n `230`; crypto_major avg `0.0734` n `8`; equity avg `0.0325` n `114`; fx avg `-0.0102` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0634` n `20`; unknown avg `-0.1171` n `792`
- 4h: commodity avg `0.433` n `12`; crypto_alt avg `0.031` n `230`; crypto_major avg `0.0897` n `8`; equity avg `-0.0504` n `114`; fx avg `0.017` n `6`; index avg `-0.1057` n `25`; metal avg `-0.1237` n `20`; unknown avg `0.0393` n `792`
- 24h: commodity avg `0.2624` n `12`; crypto_alt avg `0.0674` n `230`; crypto_major avg `0.9687` n `8`; equity avg `1.389` n `114`; fx avg `0.0135` n `6`; index avg `0.1046` n `25`; metal avg `0.1591` n `20`; unknown avg `0.1933` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1675`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1529`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0992`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0852`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0841`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `669`, weak_sample_signal
