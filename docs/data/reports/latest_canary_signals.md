# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T12:22:27.492319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1453` n `12`; crypto_alt avg `0.1317` n `228`; crypto_major avg `0.1735` n `8`; equity avg `-0.1303` n `74`; fx avg `-0.0047` n `6`; index avg `-0.0481` n `23`; metal avg `-0.1848` n `18`; unknown avg `0.1602` n `643`
- 1h: commodity avg `0.6177` n `12`; crypto_alt avg `0.1281` n `228`; crypto_major avg `0.1249` n `8`; equity avg `-0.2396` n `74`; fx avg `-0.0175` n `6`; index avg `-0.0692` n `23`; metal avg `-0.2433` n `18`; unknown avg `0.4189` n `643`
- 4h: commodity avg `0.7935` n `12`; crypto_alt avg `0.6841` n `228`; crypto_major avg `0.5332` n `8`; equity avg `-0.057` n `74`; fx avg `0.0215` n `6`; index avg `0.0796` n `23`; metal avg `-0.4695` n `18`; unknown avg `1.6808` n `643`
- 24h: commodity avg `-2.5364` n `12`; crypto_alt avg `2.6634` n `228`; crypto_major avg `2.4479` n `8`; equity avg `3.0032` n `74`; fx avg `0.0136` n `6`; index avg `1.6838` n `23`; metal avg `3.3935` n `18`; unknown avg `1.6986` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
