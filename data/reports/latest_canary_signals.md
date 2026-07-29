# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T16:22:32.176257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.71` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.1864` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0709` n `12`; crypto_alt avg `0.248` n `230`; crypto_major avg `0.1812` n `8`; equity avg `0.0908` n `102`; fx avg `0.0016` n `6`; index avg `0.047` n `25`; metal avg `0.0133` n `20`; unknown avg `0.0613` n `778`
- 1h: commodity avg `-0.0866` n `12`; crypto_alt avg `0.0548` n `230`; crypto_major avg `-0.0352` n `8`; equity avg `-0.5956` n `102`; fx avg `-0.0406` n `6`; index avg `-0.0945` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.0512` n `778`
- 4h: commodity avg `0.186` n `12`; crypto_alt avg `-0.3999` n `230`; crypto_major avg `-0.3237` n `8`; equity avg `-2.5101` n `102`; fx avg `-0.0459` n `6`; index avg `-0.3048` n `25`; metal avg `0.0268` n `20`; unknown avg `0.2865` n `777`
- 24h: commodity avg `1.4697` n `12`; crypto_alt avg `-2.5058` n `230`; crypto_major avg `-0.4691` n `8`; equity avg `-2.6064` n `102`; fx avg `-0.0926` n `6`; index avg `-0.5769` n `25`; metal avg `-0.3976` n `20`; unknown avg `-0.11` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
