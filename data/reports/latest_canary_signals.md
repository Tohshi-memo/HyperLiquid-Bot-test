# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T21:37:26.271875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0956` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.5477` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0301` n `12`; crypto_alt avg `-0.1095` n `229`; crypto_major avg `-0.1536` n `8`; equity avg `-0.1604` n `91`; fx avg `-0.009` n `6`; index avg `-0.0118` n `25`; metal avg `0.0287` n `20`; unknown avg `-0.0342` n `763`
- 1h: commodity avg `0.0643` n `12`; crypto_alt avg `-0.45` n `229`; crypto_major avg `-0.5807` n `8`; equity avg `-0.2697` n `91`; fx avg `-0.0108` n `6`; index avg `-0.0256` n `25`; metal avg `0.0521` n `20`; unknown avg `-0.0038` n `763`
- 4h: commodity avg `0.4093` n `12`; crypto_alt avg `-1.6397` n `229`; crypto_major avg `-1.6863` n `8`; equity avg `-0.9622` n `91`; fx avg `-0.0201` n `6`; index avg `-0.1386` n `25`; metal avg `-0.4082` n `20`; unknown avg `1.4267` n `761`
- 24h: commodity avg `0.9883` n `12`; crypto_alt avg `-2.9252` n `229`; crypto_major avg `-2.2179` n `8`; equity avg `-3.5135` n `91`; fx avg `-0.2561` n `6`; index avg `-0.6408` n `25`; metal avg `-0.5852` n `20`; unknown avg `-0.5405` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
