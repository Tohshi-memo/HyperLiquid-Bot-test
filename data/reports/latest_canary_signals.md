# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T04:22:29.264424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6357` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5057` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0709` n `233`; crypto_major avg `0.0475` n `8`; equity avg `-0.0625` n `136`; fx avg `-0.0001` n `6`; index avg `-0.0169` n `27`; metal avg `0.0145` n `20`; unknown avg `0.59` n `894`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.1436` n `233`; crypto_major avg `-0.0941` n `8`; equity avg `-0.1021` n `136`; fx avg `-0.0263` n `6`; index avg `-0.0252` n `27`; metal avg `-0.0392` n `20`; unknown avg `11.9759` n `886`
- 4h: commodity avg `0.0368` n `12`; crypto_alt avg `1.5475` n `233`; crypto_major avg `1.6106` n `8`; equity avg `0.1049` n `136`; fx avg `-0.0188` n `6`; index avg `0.0499` n `27`; metal avg `-0.0251` n `20`; unknown avg `13.1147` n `762`
- 24h: commodity avg `0.7037` n `12`; crypto_alt avg `-0.4579` n `233`; crypto_major avg `0.0676` n `8`; equity avg `-1.4324` n `136`; fx avg `0.0294` n `6`; index avg `-0.3297` n `26`; metal avg `-0.1415` n `20`; unknown avg `1.709` n `676`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
