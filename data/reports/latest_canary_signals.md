# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T16:52:43.814233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.05` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8727` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0748` n `12`; crypto_alt avg `0.0051` n `230`; crypto_major avg `0.0776` n `8`; equity avg `0.2112` n `102`; fx avg `0.0142` n `6`; index avg `0.0516` n `25`; metal avg `0.0322` n `20`; unknown avg `0.0066` n `778`
- 1h: commodity avg `0.0497` n `12`; crypto_alt avg `-0.0268` n `230`; crypto_major avg `-0.0832` n `8`; equity avg `0.0049` n `102`; fx avg `0.0257` n `6`; index avg `-0.0003` n `25`; metal avg `0.044` n `20`; unknown avg `-0.0318` n `778`
- 4h: commodity avg `0.2045` n `12`; crypto_alt avg `-0.4421` n `230`; crypto_major avg `-0.5197` n `8`; equity avg `-2.3924` n `102`; fx avg `-0.0374` n `6`; index avg `-0.2758` n `25`; metal avg `0.0097` n `20`; unknown avg `0.4785` n `777`
- 24h: commodity avg `1.4361` n `12`; crypto_alt avg `-2.7421` n `230`; crypto_major avg `-0.9904` n `8`; equity avg `-2.6319` n `102`; fx avg `-0.0992` n `6`; index avg `-0.5534` n `25`; metal avg `-0.2441` n `20`; unknown avg `-0.0953` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
