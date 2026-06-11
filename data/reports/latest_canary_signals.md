# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T10:22:32.679241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `-0.2802` n `228`; crypto_major avg `-0.2209` n `8`; equity avg `-0.0193` n `74`; fx avg `-0.0181` n `6`; index avg `-0.0659` n `23`; metal avg `-0.096` n `18`; unknown avg `-0.0935` n `556`
- 1h: commodity avg `-0.0871` n `12`; crypto_alt avg `0.1517` n `228`; crypto_major avg `0.0599` n `8`; equity avg `0.2295` n `74`; fx avg `-0.0405` n `6`; index avg `0.0208` n `23`; metal avg `-0.0386` n `18`; unknown avg `0.527` n `556`
- 4h: commodity avg `-0.8091` n `12`; crypto_alt avg `0.0337` n `228`; crypto_major avg `-0.1004` n `8`; equity avg `0.714` n `74`; fx avg `-0.0561` n `6`; index avg `0.2727` n `23`; metal avg `-0.1066` n `18`; unknown avg `4.7226` n `546`
- 24h: commodity avg `0.2441` n `12`; crypto_alt avg `1.7194` n `228`; crypto_major avg `1.6836` n `8`; equity avg `1.1971` n `74`; fx avg `-0.0317` n `6`; index avg `0.1702` n `23`; metal avg `-0.5246` n `18`; unknown avg `8.7405` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
