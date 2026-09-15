# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T21:08:04.454284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3856` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `-0.1504` n `233`; crypto_major avg `-0.1718` n `8`; equity avg `-0.0379` n `137`; fx avg `-0.0106` n `6`; index avg `0.0027` n `27`; metal avg `0.0135` n `20`; unknown avg `1.634` n `902`
- 1h: commodity avg `-0.0427` n `12`; crypto_alt avg `-0.2248` n `233`; crypto_major avg `-0.1822` n `8`; equity avg `-0.0185` n `137`; fx avg `-0.0176` n `6`; index avg `0.0061` n `27`; metal avg `0.0132` n `20`; unknown avg `4.245` n `884`
- 4h: commodity avg `-0.0541` n `12`; crypto_alt avg `-1.3344` n `233`; crypto_major avg `-1.3495` n `8`; equity avg `-0.2122` n `137`; fx avg `-0.0259` n `6`; index avg `0.0361` n `27`; metal avg `0.0989` n `20`; unknown avg `2.2201` n `877`
- 24h: commodity avg `0.4736` n `12`; crypto_alt avg `-4.4706` n `233`; crypto_major avg `-5.1319` n `8`; equity avg `-1.213` n `137`; fx avg `0.2072` n `6`; index avg `-0.0714` n `27`; metal avg `0.1664` n `20`; unknown avg `0.8138` n `827`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
