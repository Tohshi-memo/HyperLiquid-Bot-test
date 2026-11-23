# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T18:52:30.418327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.9554` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.4349` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.1267` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1196` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0373` n `13`; crypto_alt avg `-0.1162` n `239`; crypto_major avg `-0.1815` n `8`; equity avg `-0.3317` n `166`; fx avg `-0.0026` n `6`; index avg `-0.0337` n `27`; metal avg `0.0055` n `20`; unknown avg `2.5864` n `1266`
- 1h: commodity avg `-0.0458` n `13`; crypto_alt avg `-0.156` n `239`; crypto_major avg `-0.4639` n `8`; equity avg `-0.33` n `166`; fx avg `-0.004` n `6`; index avg `-0.0171` n `27`; metal avg `-0.0419` n `20`; unknown avg `159.5948` n `1264`
- 4h: commodity avg `-0.2649` n `13`; crypto_alt avg `-1.7088` n `239`; crypto_major avg `-2.3916` n `8`; equity avg `0.5638` n `166`; fx avg `-0.1145` n `6`; index avg `0.0433` n `27`; metal avg `-0.272` n `20`; unknown avg `7.5424` n `1258`
- 24h: commodity avg `-1.3438` n `13`; crypto_alt avg `2.3303` n `239`; crypto_major avg `2.1312` n `8`; equity avg `5.589` n `166`; fx avg `-0.0844` n `6`; index avg `0.5029` n `27`; metal avg `0.635` n `20`; unknown avg `54.6311` n `1060`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
