# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T12:59:08.353815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1927` n `12`; crypto_alt avg `0.2324` n `228`; crypto_major avg `0.2784` n `8`; equity avg `0.3338` n `74`; fx avg `0.0346` n `6`; index avg `0.1738` n `23`; metal avg `0.2732` n `18`; unknown avg `-0.0283` n `556`
- 1h: commodity avg `0.5273` n `12`; crypto_alt avg `-0.6627` n `228`; crypto_major avg `-0.6746` n `8`; equity avg `-0.5101` n `74`; fx avg `0.0176` n `6`; index avg `-0.1471` n `23`; metal avg `-0.2174` n `18`; unknown avg `0.0808` n `556`
- 4h: commodity avg `0.4937` n `12`; crypto_alt avg `-0.3325` n `228`; crypto_major avg `-0.161` n `8`; equity avg `-0.4417` n `74`; fx avg `0.005` n `6`; index avg `-0.1461` n `23`; metal avg `-0.4975` n `18`; unknown avg `0.9122` n `556`
- 24h: commodity avg `-0.1838` n `12`; crypto_alt avg `0.7559` n `228`; crypto_major avg `0.8489` n `8`; equity avg `-0.1111` n `74`; fx avg `0.0407` n `6`; index avg `-0.3517` n `23`; metal avg `-0.8133` n `18`; unknown avg `4.3569` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
