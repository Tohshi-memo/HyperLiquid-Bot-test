# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T14:22:31.766480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.0328` n `230`; crypto_major avg `0.0075` n `8`; equity avg `0.019` n `102`; fx avg `-0.008` n `6`; index avg `0.0107` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0463` n `782`
- 1h: commodity avg `-0.103` n `12`; crypto_alt avg `0.0517` n `230`; crypto_major avg `0.0598` n `8`; equity avg `0.0079` n `102`; fx avg `-0.0054` n `6`; index avg `0.0064` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0417` n `782`
- 4h: commodity avg `-0.0185` n `12`; crypto_alt avg `0.1303` n `230`; crypto_major avg `0.0932` n `8`; equity avg `-0.0509` n `102`; fx avg `-0.053` n `6`; index avg `-0.0218` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.1236` n `781`
- 24h: commodity avg `0.418` n `12`; crypto_alt avg `0.5264` n `230`; crypto_major avg `-0.712` n `8`; equity avg `-0.4247` n `102`; fx avg `-0.0003` n `6`; index avg `0.0574` n `25`; metal avg `0.185` n `20`; unknown avg `4.2971` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
