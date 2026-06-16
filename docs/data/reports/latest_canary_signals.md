# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T14:22:38.767343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0649` n `12`; crypto_alt avg `-0.6846` n `228`; crypto_major avg `-0.6799` n `8`; equity avg `-0.9613` n `77`; fx avg `0.0086` n `6`; index avg `-0.3499` n `23`; metal avg `-0.2989` n `18`; unknown avg `-0.0082` n `687`
- 1h: commodity avg `0.3819` n `12`; crypto_alt avg `-0.6337` n `228`; crypto_major avg `-0.8998` n `8`; equity avg `-0.7135` n `77`; fx avg `-0.0039` n `6`; index avg `-0.2358` n `23`; metal avg `-0.1937` n `18`; unknown avg `0.1913` n `687`
- 4h: commodity avg `0.0223` n `12`; crypto_alt avg `-1.3725` n `228`; crypto_major avg `-1.1273` n `8`; equity avg `-1.2939` n `77`; fx avg `-0.0283` n `6`; index avg `-0.5169` n `23`; metal avg `-0.2059` n `18`; unknown avg `0.6639` n `687`
- 24h: commodity avg `-0.1002` n `12`; crypto_alt avg `-1.9202` n `228`; crypto_major avg `-0.0724` n `8`; equity avg `0.183` n `77`; fx avg `-0.081` n `6`; index avg `-0.0049` n `23`; metal avg `-0.2484` n `18`; unknown avg `0.3316` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
