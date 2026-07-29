# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T14:37:27.080018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.73` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1138` n `12`; crypto_alt avg `-0.2742` n `230`; crypto_major avg `-0.2732` n `8`; equity avg `-0.5971` n `102`; fx avg `0.0298` n `6`; index avg `-0.0808` n `25`; metal avg `-0.0452` n `20`; unknown avg `-0.0273` n `778`
- 1h: commodity avg `0.1596` n `12`; crypto_alt avg `-0.427` n `230`; crypto_major avg `-0.3393` n `8`; equity avg `-1.7596` n `102`; fx avg `0.0283` n `6`; index avg `-0.2245` n `25`; metal avg `-0.0821` n `20`; unknown avg `-0.0545` n `777`
- 4h: commodity avg `0.5007` n `12`; crypto_alt avg `-0.7302` n `230`; crypto_major avg `-0.69` n `8`; equity avg `-2.1029` n `102`; fx avg `0.0336` n `6`; index avg `-0.247` n `25`; metal avg `-0.1732` n `20`; unknown avg `0.432` n `777`
- 24h: commodity avg `0.8567` n `12`; crypto_alt avg `-1.5795` n `230`; crypto_major avg `0.6734` n `8`; equity avg `-0.3919` n `102`; fx avg `-0.0211` n `6`; index avg `-0.2298` n `25`; metal avg `-0.1424` n `20`; unknown avg `-0.0736` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
