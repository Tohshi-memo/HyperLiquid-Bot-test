# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T13:52:34.935636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0988` n `13`; crypto_alt avg `0.0991` n `235`; crypto_major avg `0.1849` n `8`; equity avg `-0.3169` n `150`; fx avg `-0.0047` n `6`; index avg `-0.0267` n `26`; metal avg `0.0626` n `20`; unknown avg `-0.0629` n `1036`
- 1h: commodity avg `0.1245` n `13`; crypto_alt avg `-0.1064` n `235`; crypto_major avg `-0.2304` n `8`; equity avg `-0.605` n `150`; fx avg `0.0093` n `6`; index avg `-0.0411` n `26`; metal avg `0.212` n `20`; unknown avg `1.067` n `1034`
- 4h: commodity avg `0.3299` n `13`; crypto_alt avg `-0.7238` n `235`; crypto_major avg `-0.4876` n `8`; equity avg `-0.7138` n `150`; fx avg `-0.0546` n `6`; index avg `-0.0961` n `26`; metal avg `0.1337` n `20`; unknown avg `1.4947` n `1028`
- 24h: commodity avg `-0.1312` n `13`; crypto_alt avg `-1.2225` n `235`; crypto_major avg `-1.0595` n `8`; equity avg `-0.6669` n `150`; fx avg `0.0061` n `6`; index avg `-0.0603` n `26`; metal avg `0.6632` n `20`; unknown avg `6.8458` n `939`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
