# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T02:22:27.103891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0193` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6005` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5251` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.066` n `13`; crypto_alt avg `0.8908` n `238`; crypto_major avg `0.7867` n `8`; equity avg `0.3349` n `156`; fx avg `0.0162` n `6`; index avg `0.0296` n `27`; metal avg `-0.0107` n `20`; unknown avg `1.6752` n `1260`
- 1h: commodity avg `0.2719` n `13`; crypto_alt avg `0.3467` n `238`; crypto_major avg `0.6106` n `8`; equity avg `0.3907` n `156`; fx avg `-0.0204` n `6`; index avg `0.0021` n `27`; metal avg `0.0095` n `20`; unknown avg `4.0133` n `1254`
- 4h: commodity avg `0.234` n `13`; crypto_alt avg `-2.5293` n `238`; crypto_major avg `-1.7853` n `8`; equity avg `-0.8419` n `156`; fx avg `-0.0037` n `6`; index avg `-0.1848` n `27`; metal avg `-0.2602` n `20`; unknown avg `235.3601` n `1238`
- 24h: commodity avg `0.0625` n `13`; crypto_alt avg `-5.6234` n `238`; crypto_major avg `-1.6403` n `8`; equity avg `-3.0438` n `155`; fx avg `0.1664` n `6`; index avg `-0.2913` n `27`; metal avg `-0.7066` n `20`; unknown avg `31.336` n `988`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
