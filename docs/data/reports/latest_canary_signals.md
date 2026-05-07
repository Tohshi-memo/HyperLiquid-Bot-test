# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T17:22:22.704039+00:00`
- Correlation status: `ready`
- Asset price records: `569`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.4406` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.07` n `12`; crypto_alt avg `-0.0061` n `228`; crypto_major avg `-0.0892` n `8`; equity avg `0.0388` n `65`; fx avg `0.0005` n `5`; index avg `-0.0674` n `23`; metal avg `-0.2695` n `18`; unknown avg `-0.1377` n `365`
- 1h: commodity avg `0.0939` n `12`; crypto_alt avg `0.345` n `228`; crypto_major avg `-0.0397` n `8`; equity avg `-0.0538` n `65`; fx avg `0.015` n `5`; index avg `-0.1781` n `23`; metal avg `-0.1559` n `18`; unknown avg `1.091` n `365`
- 4h: commodity avg `1.9021` n `12`; crypto_alt avg `-1.0692` n `228`; crypto_major avg `-1.5385` n `8`; equity avg `-1.8262` n `65`; fx avg `0.0688` n `5`; index avg `-0.9603` n `23`; metal avg `-1.2624` n `18`; unknown avg `0.2563` n `365`
- 24h: commodity avg `0.3253` n `12`; crypto_alt avg `0.4194` n `228`; crypto_major avg `-2.0658` n `8`; equity avg `-0.7765` n `65`; fx avg `0.2067` n `5`; index avg `-0.5253` n `23`; metal avg `0.6876` n `18`; unknown avg `0.6384` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1355`, n `565`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `565`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1156`, n `565`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `565`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1017`, n `561`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0962`, n `561`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `561`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `561`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0849`, n `561`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `565`, weak_sample_signal
