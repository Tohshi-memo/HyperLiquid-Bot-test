# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T10:07:17.603168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1322` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.0403` n `228`; crypto_major avg `-0.0575` n `8`; equity avg `-0.051` n `67`; fx avg `-0.0031` n `6`; index avg `-0.0447` n `23`; metal avg `-0.03` n `18`; unknown avg `0.0237` n `396`
- 1h: commodity avg `0.0574` n `12`; crypto_alt avg `0.0392` n `228`; crypto_major avg `-0.0958` n `8`; equity avg `0.0332` n `67`; fx avg `-0.0031` n `6`; index avg `-0.0138` n `23`; metal avg `-0.0404` n `18`; unknown avg `0.021` n `396`
- 4h: commodity avg `-0.0477` n `12`; crypto_alt avg `-1.6663` n `228`; crypto_major avg `-1.2633` n `8`; equity avg `-0.2275` n `67`; fx avg `-0.0283` n `6`; index avg `-0.1311` n `23`; metal avg `-0.042` n `18`; unknown avg `-0.2248` n `386`
- 24h: commodity avg `-0.2782` n `12`; crypto_alt avg `-5.5237` n `228`; crypto_major avg `-3.987` n `8`; equity avg `-1.6327` n `67`; fx avg `0.0295` n `6`; index avg `-0.186` n `23`; metal avg `-0.9583` n `18`; unknown avg `-1.3155` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
