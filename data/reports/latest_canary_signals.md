# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T08:37:19.669681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3098` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0149` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.309` n `228`; crypto_major avg `-0.1159` n `8`; equity avg `0.0009` n `67`; fx avg `-0.0278` n `6`; index avg `0.0087` n `23`; metal avg `0.0143` n `18`; unknown avg `0.2387` n `386`
- 1h: commodity avg `-0.028` n `12`; crypto_alt avg `-1.8071` n `228`; crypto_major avg `-1.0492` n `8`; equity avg `-0.3069` n `67`; fx avg `-0.0674` n `6`; index avg `-0.0343` n `23`; metal avg `-0.0755` n `18`; unknown avg `-0.2841` n `386`
- 4h: commodity avg `-0.1677` n `12`; crypto_alt avg `-2.5348` n `228`; crypto_major avg `-1.5119` n `8`; equity avg `-0.4166` n `67`; fx avg `-0.0493` n `6`; index avg `-0.2021` n `23`; metal avg `-0.0171` n `18`; unknown avg `-0.5719` n `376`
- 24h: commodity avg `-0.6073` n `12`; crypto_alt avg `-6.1405` n `228`; crypto_major avg `-4.0444` n `8`; equity avg `-2.2814` n `67`; fx avg `-0.0123` n `6`; index avg `-0.3101` n `23`; metal avg `-0.564` n `18`; unknown avg `-2.6082` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
