# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T08:07:20.140263+00:00`
- Correlation status: `ready`
- Asset price records: `628`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0724` n `12`; crypto_alt avg `0.1994` n `228`; crypto_major avg `0.1135` n `8`; equity avg `0.1696` n `65`; fx avg `0.0263` n `5`; index avg `0.0519` n `23`; metal avg `-0.0374` n `18`; unknown avg `0.0601` n `375`
- 1h: commodity avg `0.2254` n `12`; crypto_alt avg `0.6053` n `228`; crypto_major avg `0.4998` n `8`; equity avg `0.3776` n `65`; fx avg `0.0198` n `5`; index avg `0.039` n `23`; metal avg `-0.3436` n `18`; unknown avg `0.0758` n `375`
- 4h: commodity avg `-0.0294` n `12`; crypto_alt avg `0.0715` n `228`; crypto_major avg `0.095` n `8`; equity avg `0.7474` n `65`; fx avg `0.1008` n `5`; index avg `0.1624` n `23`; metal avg `-0.0102` n `18`; unknown avg `0.3322` n `355`
- 24h: commodity avg `1.256` n `12`; crypto_alt avg `0.465` n `228`; crypto_major avg `-2.2278` n `8`; equity avg `-0.9377` n `65`; fx avg `0.317` n `5`; index avg `-0.7384` n `23`; metal avg `-0.8387` n `18`; unknown avg `-0.2206` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1329`, n `620`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1323`, n `620`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `624`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `624`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `624`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `624`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `620`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0804`, n `620`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `620`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `624`, weak_sample_signal
