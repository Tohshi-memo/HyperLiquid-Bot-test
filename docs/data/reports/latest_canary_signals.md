# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T20:22:15.462758+00:00`
- Correlation status: `ready`
- Asset price records: `581`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2322` n `12`; crypto_alt avg `-0.1788` n `228`; crypto_major avg `-0.1146` n `8`; equity avg `-0.4286` n `65`; fx avg `-0.0032` n `5`; index avg `0.0489` n `23`; metal avg `-0.0025` n `18`; unknown avg `-0.1099` n `365`
- 1h: commodity avg `-0.2585` n `12`; crypto_alt avg `0.4109` n `228`; crypto_major avg `0.1688` n `8`; equity avg `0.303` n `65`; fx avg `-0.001` n `5`; index avg `0.1428` n `23`; metal avg `0.4057` n `18`; unknown avg `-0.0171` n `365`
- 4h: commodity avg `0.1429` n `12`; crypto_alt avg `1.2977` n `228`; crypto_major avg `0.2043` n `8`; equity avg `0.0778` n `65`; fx avg `-0.0089` n `5`; index avg `-0.1323` n `23`; metal avg `-0.0953` n `18`; unknown avg `0.1342` n `365`
- 24h: commodity avg `0.3478` n `12`; crypto_alt avg `1.4326` n `228`; crypto_major avg `-1.8712` n `8`; equity avg `-1.5378` n `65`; fx avg `0.1852` n `5`; index avg `-0.932` n `23`; metal avg `0.3228` n `18`; unknown avg `-0.4292` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `577`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `577`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `577`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `577`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `573`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `573`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0939`, n `573`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0894`, n `573`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0821`, n `573`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0771`, n `573`, weak_sample_signal
