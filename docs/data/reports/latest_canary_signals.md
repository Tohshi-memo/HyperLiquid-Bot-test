# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T20:52:33.067706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `-0.0375` n `230`; crypto_major avg `-0.0344` n `8`; equity avg `0.0021` n `96`; fx avg `0.0007` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.0471` n `770`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `0.0137` n `230`; crypto_major avg `0.0059` n `8`; equity avg `-0.0085` n `96`; fx avg `0.0112` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.0454` n `770`
- 4h: commodity avg `0.1926` n `12`; crypto_alt avg `0.0835` n `230`; crypto_major avg `0.2538` n `8`; equity avg `-0.0177` n `96`; fx avg `-0.0092` n `6`; index avg `-0.0224` n `25`; metal avg `-0.0172` n `20`; unknown avg `-0.0629` n `770`
- 24h: commodity avg `0.3665` n `12`; crypto_alt avg `-0.2852` n `230`; crypto_major avg `0.399` n `8`; equity avg `-0.2678` n `96`; fx avg `-0.0965` n `6`; index avg `0.0391` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0178` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
