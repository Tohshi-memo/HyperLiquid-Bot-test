# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T04:37:24.164554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.0246` n `230`; crypto_major avg `-0.0036` n `8`; equity avg `-0.0728` n `94`; fx avg `-0.011` n `6`; index avg `-0.0205` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.1055` n `768`
- 1h: commodity avg `0.0471` n `12`; crypto_alt avg `-0.1028` n `230`; crypto_major avg `-0.0859` n `8`; equity avg `-0.2141` n `94`; fx avg `0.0004` n `6`; index avg `-0.034` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.2586` n `768`
- 4h: commodity avg `-0.1026` n `12`; crypto_alt avg `0.0385` n `230`; crypto_major avg `0.0766` n `8`; equity avg `-0.0961` n `94`; fx avg `-0.0312` n `6`; index avg `-0.0502` n `25`; metal avg `-0.1277` n `20`; unknown avg `-0.4512` n `768`
- 24h: commodity avg `-0.0721` n `12`; crypto_alt avg `0.1748` n `230`; crypto_major avg `0.0512` n `8`; equity avg `-2.4987` n `93`; fx avg `0.0925` n `6`; index avg `-0.4976` n `25`; metal avg `0.0449` n `20`; unknown avg `-0.2029` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
