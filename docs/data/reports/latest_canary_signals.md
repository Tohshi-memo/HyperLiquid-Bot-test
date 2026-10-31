# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T07:22:26.111612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `13`; crypto_alt avg `0.0417` n `238`; crypto_major avg `0.0191` n `8`; equity avg `-0.0123` n `156`; fx avg `-0.0037` n `6`; index avg `-0.0033` n `27`; metal avg `-0.0038` n `20`; unknown avg `-0.0139` n `1262`
- 1h: commodity avg `-0.0036` n `13`; crypto_alt avg `-0.0907` n `238`; crypto_major avg `0.0218` n `8`; equity avg `0.0204` n `156`; fx avg `0.0025` n `6`; index avg `-0.0092` n `27`; metal avg `-0.001` n `20`; unknown avg `4.4046` n `1252`
- 4h: commodity avg `-0.0061` n `13`; crypto_alt avg `-0.6852` n `238`; crypto_major avg `-0.5281` n `8`; equity avg `-0.023` n `156`; fx avg `0.0103` n `6`; index avg `-0.0268` n `27`; metal avg `0.0126` n `20`; unknown avg `0.437` n `1216`
- 24h: commodity avg `-0.0109` n `13`; crypto_alt avg `0.8467` n `238`; crypto_major avg `-1.565` n `8`; equity avg `-2.3632` n `156`; fx avg `-0.0553` n `6`; index avg `-0.2376` n `27`; metal avg `-0.4582` n `20`; unknown avg `3.9681` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
