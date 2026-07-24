# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T19:07:35.295806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0695` n `12`; crypto_alt avg `-0.1571` n `230`; crypto_major avg `-0.1303` n `8`; equity avg `-0.3724` n `100`; fx avg `0.0021` n `6`; index avg `-0.0329` n `25`; metal avg `-0.0328` n `20`; unknown avg `-0.1436` n `773`
- 1h: commodity avg `0.1476` n `12`; crypto_alt avg `-0.2363` n `230`; crypto_major avg `-0.1472` n `8`; equity avg `-0.8605` n `100`; fx avg `0.0041` n `6`; index avg `-0.1605` n `25`; metal avg `-0.1054` n `20`; unknown avg `-0.1498` n `773`
- 4h: commodity avg `-0.2444` n `12`; crypto_alt avg `0.2638` n `230`; crypto_major avg `0.2009` n `8`; equity avg `-0.8528` n `100`; fx avg `-0.0169` n `6`; index avg `-0.118` n `25`; metal avg `-0.0666` n `20`; unknown avg `-0.155` n `773`
- 24h: commodity avg `-0.4281` n `12`; crypto_alt avg `-0.9797` n `230`; crypto_major avg `-0.8871` n `8`; equity avg `-2.9807` n `100`; fx avg `-0.1532` n `6`; index avg `-0.3641` n `25`; metal avg `0.0403` n `20`; unknown avg `14.1599` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1262`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1215`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1129`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `666`, weak_sample_signal
