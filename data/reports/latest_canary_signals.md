# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T23:07:35.633604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.39` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1152` n `12`; crypto_alt avg `-0.2229` n `230`; crypto_major avg `-0.2366` n `8`; equity avg `-0.2761` n `102`; fx avg `-0.0162` n `6`; index avg `-0.011` n `25`; metal avg `0.0063` n `20`; unknown avg `0.5286` n `776`
- 1h: commodity avg `0.3654` n `12`; crypto_alt avg `-0.7165` n `230`; crypto_major avg `-0.8109` n `8`; equity avg `-1.3219` n `102`; fx avg `-0.0222` n `6`; index avg `-0.1948` n `25`; metal avg `-0.0594` n `20`; unknown avg `0.6975` n `776`
- 4h: commodity avg `0.7933` n `12`; crypto_alt avg `-0.498` n `230`; crypto_major avg `-0.4011` n `8`; equity avg `-0.5924` n `102`; fx avg `-0.0283` n `6`; index avg `-0.1598` n `25`; metal avg `-0.0854` n `20`; unknown avg `0.761` n `776`
- 24h: commodity avg `-0.1519` n `12`; crypto_alt avg `-0.7298` n `230`; crypto_major avg `-0.4265` n `8`; equity avg `-3.3625` n `102`; fx avg `-0.1013` n `6`; index avg `-0.4814` n `25`; metal avg `-0.4643` n `20`; unknown avg `0.226` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
