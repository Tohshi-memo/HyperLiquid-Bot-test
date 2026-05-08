# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T06:52:20.083710+00:00`
- Correlation status: `ready`
- Asset price records: `623`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1825` n `12`; crypto_alt avg `0.1237` n `228`; crypto_major avg `0.1185` n `8`; equity avg `0.0005` n `65`; fx avg `-0.0207` n `5`; index avg `0.0158` n `23`; metal avg `-0.0611` n `18`; unknown avg `0.0073` n `375`
- 1h: commodity avg `-0.1227` n `12`; crypto_alt avg `-0.2459` n `228`; crypto_major avg `-0.2083` n `8`; equity avg `0.1971` n `65`; fx avg `0.0303` n `5`; index avg `0.0732` n `23`; metal avg `0.172` n `18`; unknown avg `-0.0561` n `355`
- 4h: commodity avg `-0.1346` n `12`; crypto_alt avg `0.0513` n `228`; crypto_major avg `-0.2116` n `8`; equity avg `0.5615` n `65`; fx avg `0.1051` n `5`; index avg `0.1818` n `23`; metal avg `0.6421` n `18`; unknown avg `-0.0328` n `355`
- 24h: commodity avg `0.5645` n `12`; crypto_alt avg `0.6034` n `228`; crypto_major avg `-2.1166` n `8`; equity avg `-1.0022` n `65`; fx avg `0.3011` n `5`; index avg `-0.6227` n `23`; metal avg `0.2359` n `18`; unknown avg `-0.1898` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.134`, n `615`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1331`, n `615`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `619`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `619`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `619`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0939`, n `619`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `615`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0819`, n `615`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `615`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `619`, weak_sample_signal
