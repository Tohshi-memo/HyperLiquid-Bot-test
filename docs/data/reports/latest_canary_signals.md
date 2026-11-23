# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T18:07:33.053853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8239` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.666` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6036` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0031` n `13`; crypto_alt avg `0.1154` n `239`; crypto_major avg `-0.1064` n `8`; equity avg `0.182` n `166`; fx avg `-0.0065` n `6`; index avg `0.0282` n `27`; metal avg `0.0333` n `20`; unknown avg `160.4281` n `1258`
- 1h: commodity avg `0.0388` n `13`; crypto_alt avg `-0.3902` n `239`; crypto_major avg `-0.5344` n `8`; equity avg `-0.1681` n `166`; fx avg `-0.0132` n `6`; index avg `-0.01` n `27`; metal avg `-0.0719` n `20`; unknown avg `317.4787` n `1264`
- 4h: commodity avg `-0.328` n `13`; crypto_alt avg `-0.6431` n `239`; crypto_major avg `-1.8323` n `8`; equity avg `-0.2287` n `166`; fx avg `-0.1372` n `6`; index avg `-0.0084` n `27`; metal avg `-0.1663` n `20`; unknown avg `326.2996` n `1256`
- 24h: commodity avg `-1.2774` n `13`; crypto_alt avg `2.443` n `239`; crypto_major avg `2.5776` n `8`; equity avg `5.9526` n `166`; fx avg `-0.0837` n `6`; index avg `0.5497` n `27`; metal avg `0.6667` n `20`; unknown avg `122.2401` n `1064`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
