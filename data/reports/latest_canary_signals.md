# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T19:52:16.595715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4348` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0405` n `12`; crypto_alt avg `0.2037` n `228`; crypto_major avg `0.1404` n `8`; equity avg `-0.1423` n `67`; fx avg `0.0104` n `6`; index avg `-0.0848` n `23`; metal avg `0.0081` n `18`; unknown avg `-0.0949` n `386`
- 1h: commodity avg `0.157` n `12`; crypto_alt avg `-0.9694` n `228`; crypto_major avg `-0.6285` n `8`; equity avg `-0.5652` n `67`; fx avg `0.0368` n `6`; index avg `-0.2392` n `23`; metal avg `-0.1783` n `18`; unknown avg `0.842` n `386`
- 4h: commodity avg `-0.0887` n `12`; crypto_alt avg `-2.6142` n `228`; crypto_major avg `-1.6224` n `8`; equity avg `-0.9181` n `67`; fx avg `0.0729` n `6`; index avg `-0.1876` n `23`; metal avg `-0.1335` n `18`; unknown avg `0.6525` n `386`
- 24h: commodity avg `-0.893` n `12`; crypto_alt avg `-2.9737` n `228`; crypto_major avg `-2.2721` n `8`; equity avg `-0.8326` n `67`; fx avg `0.1912` n `6`; index avg `0.5665` n `23`; metal avg `-0.9938` n `18`; unknown avg `-1.5388` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
