# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T03:22:23.712839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.3183` n `230`; crypto_major avg `0.1385` n `8`; equity avg `0.1956` n `94`; fx avg `0.0025` n `6`; index avg `0.0505` n `25`; metal avg `0.0852` n `20`; unknown avg `0.0475` n `768`
- 1h: commodity avg `-0.065` n `12`; crypto_alt avg `0.5992` n `230`; crypto_major avg `0.2841` n `8`; equity avg `0.1526` n `94`; fx avg `0.0231` n `6`; index avg `0.0415` n `25`; metal avg `0.0966` n `20`; unknown avg `-0.1171` n `768`
- 4h: commodity avg `-0.0546` n `12`; crypto_alt avg `0.3938` n `230`; crypto_major avg `0.1455` n `8`; equity avg `-1.0303` n `94`; fx avg `-0.0048` n `6`; index avg `-0.1733` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.1539` n `768`
- 24h: commodity avg `-0.1087` n `12`; crypto_alt avg `-1.6499` n `230`; crypto_major avg `-2.661` n `8`; equity avg `-5.1077` n `94`; fx avg `-0.1321` n `6`; index avg `-0.6181` n `25`; metal avg `-0.6519` n `20`; unknown avg `-0.6235` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
