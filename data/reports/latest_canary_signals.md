# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T10:37:26.035486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0511` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `0.0119` n `8`; equity avg `0.1004` n `112`; fx avg `-0.0046` n `6`; index avg `0.0217` n `25`; metal avg `0.0462` n `20`; unknown avg `-0.0126` n `782`
- 1h: commodity avg `-0.1134` n `12`; crypto_alt avg `0.0024` n `230`; crypto_major avg `-0.0502` n `8`; equity avg `-0.1065` n `112`; fx avg `-0.0164` n `6`; index avg `-0.013` n `25`; metal avg `-0.0209` n `20`; unknown avg `0.0958` n `782`
- 4h: commodity avg `-0.2985` n `12`; crypto_alt avg `0.014` n `230`; crypto_major avg `0.6393` n `8`; equity avg `0.4489` n `112`; fx avg `-0.0323` n `6`; index avg `0.0665` n `25`; metal avg `0.1387` n `20`; unknown avg `0.1251` n `782`
- 24h: commodity avg `0.1888` n `12`; crypto_alt avg `0.6654` n `230`; crypto_major avg `0.2505` n `8`; equity avg `1.9436` n `109`; fx avg `-0.0872` n `6`; index avg `0.0467` n `25`; metal avg `0.2956` n `20`; unknown avg `0.3078` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
