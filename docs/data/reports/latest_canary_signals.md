# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T02:37:23.607636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0932` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0368` n `12`; crypto_alt avg `-0.0312` n `231`; crypto_major avg `-0.0198` n `8`; equity avg `-0.0943` n `128`; fx avg `-0.0079` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0455` n `20`; unknown avg `-0.0051` n `793`
- 1h: commodity avg `0.085` n `12`; crypto_alt avg `0.1748` n `231`; crypto_major avg `0.0283` n `8`; equity avg `-0.0774` n `128`; fx avg `-0.01` n `6`; index avg `0.0022` n `26`; metal avg `-0.1652` n `20`; unknown avg `-0.0613` n `779`
- 4h: commodity avg `0.1068` n `12`; crypto_alt avg `-1.0825` n `231`; crypto_major avg `-1.292` n `8`; equity avg `-1.0318` n `128`; fx avg `-0.0523` n `6`; index avg `-0.1988` n `26`; metal avg `-0.3784` n `20`; unknown avg `0.4324` n `779`
- 24h: commodity avg `0.4388` n `12`; crypto_alt avg `-0.4494` n `231`; crypto_major avg `-1.9872` n `8`; equity avg `-1.309` n `128`; fx avg `-0.0396` n `6`; index avg `-0.2785` n `26`; metal avg `-0.4712` n `20`; unknown avg `-0.4904` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
