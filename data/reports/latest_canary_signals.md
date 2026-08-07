# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T19:37:34.366402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.0432` n `230`; crypto_major avg `0.005` n `8`; equity avg `-0.1938` n `112`; fx avg `-0.0076` n `6`; index avg `-0.0213` n `25`; metal avg `-0.0301` n `20`; unknown avg `-0.0346` n `782`
- 1h: commodity avg `-0.269` n `12`; crypto_alt avg `0.1574` n `230`; crypto_major avg `0.3897` n `8`; equity avg `0.1976` n `112`; fx avg `-0.0141` n `6`; index avg `0.0757` n `25`; metal avg `0.0706` n `20`; unknown avg `-0.0683` n `782`
- 4h: commodity avg `-0.2617` n `12`; crypto_alt avg `-0.1465` n `230`; crypto_major avg `-0.3709` n `8`; equity avg `-0.2271` n `112`; fx avg `-0.0234` n `6`; index avg `-0.0097` n `25`; metal avg `0.0584` n `20`; unknown avg `-0.2321` n `782`
- 24h: commodity avg `-0.1001` n `12`; crypto_alt avg `-0.0361` n `230`; crypto_major avg `0.0432` n `8`; equity avg `1.5505` n `112`; fx avg `-0.149` n `6`; index avg `0.0842` n `25`; metal avg `0.4325` n `20`; unknown avg `0.0231` n `765`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
