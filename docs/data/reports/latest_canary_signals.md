# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T03:22:23.382718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0237` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `0.2034` n `231`; crypto_major avg `0.2087` n `8`; equity avg `0.1296` n `128`; fx avg `0.0065` n `6`; index avg `0.0152` n `26`; metal avg `0.0625` n `20`; unknown avg `0.0882` n `793`
- 1h: commodity avg `-0.0615` n `12`; crypto_alt avg `0.1527` n `231`; crypto_major avg `-0.057` n `8`; equity avg `0.1184` n `128`; fx avg `-0.0023` n `6`; index avg `0.0644` n `26`; metal avg `0.1062` n `20`; unknown avg `-0.1685` n `791`
- 4h: commodity avg `0.0814` n `12`; crypto_alt avg `-0.6271` n `231`; crypto_major avg `-1.0838` n `8`; equity avg `-0.3836` n `128`; fx avg `-0.049` n `6`; index avg `-0.0601` n `26`; metal avg `-0.2776` n `20`; unknown avg `1.8331` n `779`
- 24h: commodity avg `0.3421` n `12`; crypto_alt avg `-0.4436` n `231`; crypto_major avg `-1.9813` n `8`; equity avg `-1.0859` n `128`; fx avg `-0.0372` n `6`; index avg `-0.2025` n `26`; metal avg `-0.3159` n `20`; unknown avg `-0.4434` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
