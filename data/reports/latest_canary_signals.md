# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T11:07:24.513042+00:00`
- Correlation status: `ready`
- Asset price records: `544`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2201` n `12`; crypto_alt avg `0.1487` n `228`; crypto_major avg `0.1194` n `8`; equity avg `0.1561` n `65`; fx avg `-0.0087` n `4`; index avg `-0.02` n `23`; metal avg `-0.0397` n `18`; unknown avg `0.3019` n `366`
- 1h: commodity avg `-0.2178` n `12`; crypto_alt avg `0.0719` n `228`; crypto_major avg `-0.077` n `8`; equity avg `0.0856` n `65`; fx avg `0.0195` n `4`; index avg `0.0577` n `23`; metal avg `-0.0154` n `18`; unknown avg `0.2325` n `366`
- 4h: commodity avg `-0.1321` n `12`; crypto_alt avg `0.0297` n `228`; crypto_major avg `-0.2876` n `8`; equity avg `0.1467` n `65`; fx avg `0.1246` n `4`; index avg `-0.0859` n `23`; metal avg `0.3592` n `18`; unknown avg `0.5611` n `358`
- 24h: commodity avg `0.635` n `7`; crypto_alt avg `-0.1247` n `223`; crypto_major avg `-2.3749` n `7`; equity avg `-0.0046` n `47`; fx avg `0.2379` n `4`; index avg `0.1785` n `6`; metal avg `0.9186` n `7`; unknown avg `0.7427` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1308`, n `540`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1231`, n `540`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0928`, n `540`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `536`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0806`, n `536`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `536`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0768`, n `536`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `540`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0713`, n `536`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `536`, weak_sample_signal
