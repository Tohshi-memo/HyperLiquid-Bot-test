# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T12:52:29.534503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.248` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0323` n `13`; crypto_alt avg `-0.0782` n `239`; crypto_major avg `-0.2215` n `8`; equity avg `-0.2327` n `158`; fx avg `0.0101` n `6`; index avg `-0.0114` n `27`; metal avg `0.0761` n `20`; unknown avg `0.0941` n `1255`
- 1h: commodity avg `0.0435` n `13`; crypto_alt avg `-0.9356` n `239`; crypto_major avg `-0.9837` n `8`; equity avg `-0.9965` n `158`; fx avg `0.0392` n `6`; index avg `-0.0724` n `27`; metal avg `-0.0451` n `20`; unknown avg `0.494` n `1245`
- 4h: commodity avg `0.4178` n `13`; crypto_alt avg `-1.6082` n `239`; crypto_major avg `-1.2771` n `8`; equity avg `-0.9501` n `158`; fx avg `0.0202` n `6`; index avg `-0.0291` n `27`; metal avg `0.0601` n `20`; unknown avg `38.0696` n `1145`
- 24h: commodity avg `-1.1544` n `13`; crypto_alt avg `-0.0628` n `239`; crypto_major avg `1.1734` n `8`; equity avg `-2.4156` n `158`; fx avg `-0.0132` n `6`; index avg `-0.2451` n `27`; metal avg `0.6504` n `20`; unknown avg `39.9944` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2415`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
