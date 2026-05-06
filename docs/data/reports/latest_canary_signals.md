# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T17:52:18.258534+00:00`
- Correlation status: `ready`
- Asset price records: `475`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.64` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `-0.0506` n `228`; crypto_major avg `-0.1165` n `8`; equity avg `-0.1271` n `65`; fx avg `0.0237` n `4`; index avg `-0.034` n `23`; metal avg `0.0016` n `18`; unknown avg `0.0297` n `356`
- 1h: commodity avg `-0.1773` n `12`; crypto_alt avg `-0.389` n `228`; crypto_major avg `-0.432` n `8`; equity avg `0.1614` n `65`; fx avg `-0.0289` n `4`; index avg `0.0852` n `23`; metal avg `-0.1378` n `18`; unknown avg `-0.4236` n `356`
- 4h: commodity avg `-0.1072` n `12`; crypto_alt avg `0.2645` n `228`; crypto_major avg `-0.3093` n `8`; equity avg `0.7746` n `65`; fx avg `0.0286` n `4`; index avg `0.4158` n `23`; metal avg `-0.0102` n `18`; unknown avg `0.4785` n `356`
- 24h: commodity avg `-2.3826` n `7`; crypto_alt avg `2.833` n `223`; crypto_major avg `0.5441` n `7`; equity avg `2.3871` n `47`; fx avg `-0.4428` n `4`; index avg `1.7379` n `6`; metal avg `2.9058` n `7`; unknown avg `4.5561` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1487`, n `467`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1329`, n `467`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `471`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `471`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `471`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1132`, n `467`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0995`, n `467`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0922`, n `471`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `467`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `467`, weak_sample_signal
