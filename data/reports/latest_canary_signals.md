# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T11:22:27.107784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0418` n `12`; crypto_alt avg `0.0789` n `232`; crypto_major avg `-0.0146` n `8`; equity avg `-0.0251` n `128`; fx avg `-0.0056` n `6`; index avg `0.0061` n `26`; metal avg `0.0262` n `20`; unknown avg `0.0422` n `794`
- 1h: commodity avg `-0.0222` n `12`; crypto_alt avg `0.4594` n `232`; crypto_major avg `0.4902` n `8`; equity avg `0.0208` n `128`; fx avg `-0.0305` n `6`; index avg `0.007` n `26`; metal avg `0.1253` n `20`; unknown avg `0.1528` n `792`
- 4h: commodity avg `0.4297` n `12`; crypto_alt avg `0.0103` n `232`; crypto_major avg `0.5709` n `8`; equity avg `-0.3052` n `128`; fx avg `-0.0385` n `6`; index avg `-0.0374` n `26`; metal avg `0.0808` n `20`; unknown avg `0.1514` n `791`
- 24h: commodity avg `0.6905` n `12`; crypto_alt avg `-0.2088` n `231`; crypto_major avg `-0.7942` n `8`; equity avg `-0.4881` n `128`; fx avg `-0.1421` n `6`; index avg `-0.0941` n `26`; metal avg `-0.1164` n `20`; unknown avg `0.0585` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
