# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T16:37:20.958225+00:00`
- Correlation status: `ready`
- Asset price records: `566`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.4557` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1256` n `12`; crypto_alt avg `0.1398` n `228`; crypto_major avg `-0.0005` n `8`; equity avg `0.3396` n `65`; fx avg `0.003` n `5`; index avg `0.1507` n `23`; metal avg `0.1439` n `18`; unknown avg `0.4598` n `365`
- 1h: commodity avg `1.0591` n `12`; crypto_alt avg `0.0394` n `228`; crypto_major avg `-0.2193` n `8`; equity avg `-0.965` n `65`; fx avg `0.0176` n `5`; index avg `-0.4742` n `23`; metal avg `-0.7374` n `18`; unknown avg `-0.0577` n `365`
- 4h: commodity avg `1.8611` n `12`; crypto_alt avg `-1.2148` n `228`; crypto_major avg `-1.5946` n `8`; equity avg `-1.3451` n `65`; fx avg `0.0742` n `5`; index avg `-0.696` n `23`; metal avg `-1.0701` n `18`; unknown avg `-0.2437` n `365`
- 24h: commodity avg `0.4596` n `12`; crypto_alt avg `0.4274` n `228`; crypto_major avg `-1.9982` n `8`; equity avg `-0.2735` n `65`; fx avg `0.1475` n `5`; index avg `-0.1273` n `23`; metal avg `0.7485` n `18`; unknown avg `-0.1349` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1331`, n `562`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `562`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `562`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `562`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0971`, n `558`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0918`, n `558`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `558`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `558`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0792`, n `558`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `562`, weak_sample_signal
