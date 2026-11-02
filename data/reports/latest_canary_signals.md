# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T17:37:26.165881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1985` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1238` n `13`; crypto_alt avg `-0.3057` n `239`; crypto_major avg `-0.2163` n `8`; equity avg `-0.2637` n `156`; fx avg `-0.0072` n `6`; index avg `-0.0198` n `27`; metal avg `-0.0632` n `20`; unknown avg `30.5379` n `1265`
- 1h: commodity avg `-0.2081` n `13`; crypto_alt avg `-0.9684` n `239`; crypto_major avg `-0.862` n `8`; equity avg `-0.5344` n `156`; fx avg `0.0028` n `6`; index avg `-0.0333` n `27`; metal avg `-0.0974` n `20`; unknown avg `0.0766` n `1257`
- 4h: commodity avg `-0.6167` n `13`; crypto_alt avg `-1.3763` n `239`; crypto_major avg `-1.2744` n `8`; equity avg `-1.6477` n `156`; fx avg `0.0103` n `6`; index avg `-0.0759` n `27`; metal avg `0.2166` n `20`; unknown avg `15.118` n `1251`
- 24h: commodity avg `-1.3026` n `13`; crypto_alt avg `-3.0572` n `238`; crypto_major avg `-1.7351` n `8`; equity avg `-1.3222` n `156`; fx avg `0.2812` n `6`; index avg `0.174` n `27`; metal avg `0.3183` n `20`; unknown avg `8.2359` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
