# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T01:52:30.734764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.2045` n `232`; crypto_major avg `-0.0988` n `8`; equity avg `0.0678` n `134`; fx avg `0.0249` n `6`; index avg `0.0011` n `26`; metal avg `0.0243` n `20`; unknown avg `2.7545` n `794`
- 1h: commodity avg `-0.0452` n `12`; crypto_alt avg `-1.0335` n `232`; crypto_major avg `-0.704` n `8`; equity avg `-0.0345` n `134`; fx avg `0.059` n `6`; index avg `0.0199` n `26`; metal avg `-0.0237` n `20`; unknown avg `1.7546` n `792`
- 4h: commodity avg `-0.0459` n `12`; crypto_alt avg `-0.851` n `232`; crypto_major avg `-0.5606` n `8`; equity avg `0.033` n `134`; fx avg `-0.0541` n `6`; index avg `0.0072` n `26`; metal avg `-0.035` n `20`; unknown avg `1.6757` n `783`
- 24h: commodity avg `-0.0587` n `12`; crypto_alt avg `-0.3574` n `232`; crypto_major avg `-0.1837` n `8`; equity avg `0.2716` n `134`; fx avg `-0.0113` n `6`; index avg `0.0397` n `26`; metal avg `-0.0747` n `20`; unknown avg `152.2812` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
