# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T02:37:25.155223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `0.1205` n `230`; crypto_major avg `0.0929` n `8`; equity avg `0.1392` n `98`; fx avg `-0.0108` n `6`; index avg `0.0852` n `25`; metal avg `0.0561` n `20`; unknown avg `-0.0374` n `769`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `-0.2196` n `230`; crypto_major avg `-0.2702` n `8`; equity avg `-0.1506` n `98`; fx avg `-0.013` n `6`; index avg `-0.0026` n `25`; metal avg `0.1026` n `20`; unknown avg `0.1321` n `769`
- 4h: commodity avg `-0.1023` n `12`; crypto_alt avg `0.152` n `230`; crypto_major avg `0.0839` n `8`; equity avg `-0.2532` n `98`; fx avg `-0.0556` n `6`; index avg `0.0386` n `25`; metal avg `0.2175` n `20`; unknown avg `0.5411` n `767`
- 24h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.1292` n `230`; crypto_major avg `-0.1757` n `8`; equity avg `0.1037` n `97`; fx avg `-0.0218` n `6`; index avg `0.0605` n `25`; metal avg `0.0579` n `20`; unknown avg `0.0396` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1215`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1038`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `667`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1019`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0855`, n `667`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `667`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.08`, n `667`, weak_sample_signal
