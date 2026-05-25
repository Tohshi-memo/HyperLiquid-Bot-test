# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T08:37:14.022690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `0.0801` n `228`; crypto_major avg `0.1302` n `8`; equity avg `0.0039` n `67`; fx avg `-0.0054` n `6`; index avg `-0.0059` n `23`; metal avg `0.0671` n `18`; unknown avg `0.043` n `397`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `0.2133` n `228`; crypto_major avg `0.4027` n `8`; equity avg `0.0419` n `67`; fx avg `0.0156` n `6`; index avg `-0.0227` n `23`; metal avg `0.0382` n `18`; unknown avg `0.1538` n `397`
- 4h: commodity avg `0.4374` n `12`; crypto_alt avg `0.9111` n `228`; crypto_major avg `0.8108` n `8`; equity avg `0.1167` n `67`; fx avg `0.0724` n `6`; index avg `0.0009` n `23`; metal avg `-0.0225` n `18`; unknown avg `0.0975` n `387`
- 24h: commodity avg `0.2395` n `12`; crypto_alt avg `0.1078` n `228`; crypto_major avg `0.1523` n `8`; equity avg `0.5246` n `67`; fx avg `0.0007` n `6`; index avg `-0.1085` n `23`; metal avg `0.4463` n `18`; unknown avg `-0.2247` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
