# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T00:52:33.373805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0235` n `13`; crypto_alt avg `-0.4107` n `236`; crypto_major avg `-0.245` n `8`; equity avg `-0.2222` n `151`; fx avg `0.0231` n `6`; index avg `-0.0467` n `26`; metal avg `-0.004` n `20`; unknown avg `2.1592` n `1136`
- 1h: commodity avg `-0.0843` n `13`; crypto_alt avg `-0.444` n `236`; crypto_major avg `-0.1034` n `8`; equity avg `0.1739` n `151`; fx avg `0.1039` n `6`; index avg `-0.0845` n `26`; metal avg `0.157` n `20`; unknown avg `0.9896` n `1128`
- 4h: commodity avg `-0.1318` n `13`; crypto_alt avg `-0.2383` n `236`; crypto_major avg `-0.0892` n `8`; equity avg `-1.2649` n `151`; fx avg `0.1587` n `6`; index avg `-0.2986` n `26`; metal avg `0.1995` n `20`; unknown avg `2.7869` n `1040`
- 24h: commodity avg `-0.3807` n `13`; crypto_alt avg `-3.0269` n `236`; crypto_major avg `-2.485` n `8`; equity avg `-5.745` n `151`; fx avg `0.0132` n `6`; index avg `-0.9019` n `26`; metal avg `-0.6028` n `20`; unknown avg `1393.4528` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.101`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0794`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
