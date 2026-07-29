# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T01:37:31.859693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0796` n `12`; crypto_alt avg `-0.0955` n `230`; crypto_major avg `-0.0852` n `8`; equity avg `0.0138` n `102`; fx avg `0.0147` n `6`; index avg `-0.0045` n `25`; metal avg `0.1255` n `20`; unknown avg `0.1774` n `777`
- 1h: commodity avg `0.1307` n `12`; crypto_alt avg `-0.4301` n `230`; crypto_major avg `-0.2053` n `8`; equity avg `-0.68` n `102`; fx avg `-0.0004` n `6`; index avg `-0.1516` n `25`; metal avg `0.0138` n `20`; unknown avg `0.0631` n `777`
- 4h: commodity avg `0.6342` n `12`; crypto_alt avg `-0.5748` n `230`; crypto_major avg `-0.2477` n `8`; equity avg `-0.3657` n `102`; fx avg `0.0063` n `6`; index avg `-0.0728` n `25`; metal avg `0.0476` n `20`; unknown avg `0.1833` n `776`
- 24h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.0077` n `230`; crypto_major avg `0.5868` n `8`; equity avg `-1.6936` n `102`; fx avg `-0.1443` n `6`; index avg `-0.1598` n `25`; metal avg `-0.0869` n `20`; unknown avg `-0.085` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
