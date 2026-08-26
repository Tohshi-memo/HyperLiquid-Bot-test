# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T18:08:22.743048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0626` n `12`; crypto_alt avg `0.1099` n `231`; crypto_major avg `0.1268` n `8`; equity avg `0.0529` n `122`; fx avg `-0.0012` n `6`; index avg `0.0054` n `25`; metal avg `0.0283` n `20`; unknown avg `0.0014` n `797`
- 1h: commodity avg `-0.1653` n `12`; crypto_alt avg `0.4101` n `231`; crypto_major avg `0.6717` n `8`; equity avg `0.2669` n `122`; fx avg `-0.0044` n `6`; index avg `0.0291` n `25`; metal avg `0.0349` n `20`; unknown avg `0.2252` n `797`
- 4h: commodity avg `0.1906` n `12`; crypto_alt avg `-0.7557` n `231`; crypto_major avg `-0.4047` n `8`; equity avg `-0.2106` n `122`; fx avg `-0.0033` n `6`; index avg `-0.0271` n `25`; metal avg `-0.1786` n `20`; unknown avg `-0.0848` n `797`
- 24h: commodity avg `0.2309` n `12`; crypto_alt avg `-1.9111` n `231`; crypto_major avg `-1.7618` n `8`; equity avg `0.0099` n `122`; fx avg `-0.0479` n `6`; index avg `0.0578` n `25`; metal avg `-0.2858` n `20`; unknown avg `0.5257` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
