# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T02:52:26.423247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2678` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0981` n `12`; crypto_alt avg `-0.9294` n `228`; crypto_major avg `-0.53` n `8`; equity avg `-0.1628` n `74`; fx avg `-0.0173` n `6`; index avg `-0.1498` n `23`; metal avg `0.1436` n `18`; unknown avg `-0.398` n `424`
- 1h: commodity avg `0.2136` n `12`; crypto_alt avg `-1.8259` n `228`; crypto_major avg `-1.2551` n `8`; equity avg `-0.0275` n `74`; fx avg `-0.0476` n `6`; index avg `0.0127` n `23`; metal avg `0.1496` n `18`; unknown avg `-0.1854` n `424`
- 4h: commodity avg `0.2109` n `12`; crypto_alt avg `-1.4836` n `228`; crypto_major avg `-0.9299` n `8`; equity avg `-0.6608` n `74`; fx avg `0.1193` n `6`; index avg `-0.5739` n `23`; metal avg `-0.775` n `18`; unknown avg `0.1396` n `424`
- 24h: commodity avg `0.0475` n `12`; crypto_alt avg `-4.666` n `228`; crypto_major avg `-3.5132` n `8`; equity avg `-0.9721` n `73`; fx avg `0.1997` n `6`; index avg `-0.3202` n `23`; metal avg `-0.4292` n `18`; unknown avg `-0.9586` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
