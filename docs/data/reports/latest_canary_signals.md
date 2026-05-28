# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T19:07:21.446227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0571` n `12`; crypto_alt avg `-0.2118` n `228`; crypto_major avg `-0.2406` n `8`; equity avg `-0.0722` n `69`; fx avg `0.0027` n `6`; index avg `0.0613` n `23`; metal avg `0.0161` n `18`; unknown avg `0.1742` n `417`
- 1h: commodity avg `0.3091` n `12`; crypto_alt avg `-0.2164` n `228`; crypto_major avg `0.0105` n `8`; equity avg `0.0878` n `69`; fx avg `0.0114` n `6`; index avg `-0.0187` n `23`; metal avg `-0.1906` n `18`; unknown avg `0.2619` n `417`
- 4h: commodity avg `0.2126` n `12`; crypto_alt avg `1.8955` n `228`; crypto_major avg `1.6584` n `8`; equity avg `0.7987` n `69`; fx avg `0.0135` n `6`; index avg `0.4614` n `23`; metal avg `0.6146` n `18`; unknown avg `0.5283` n `417`
- 24h: commodity avg `1.1753` n `12`; crypto_alt avg `-3.4627` n `228`; crypto_major avg `-0.9316` n `8`; equity avg `1.6806` n `69`; fx avg `-0.018` n `6`; index avg `0.9738` n `23`; metal avg `0.5608` n `18`; unknown avg `-0.6494` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
