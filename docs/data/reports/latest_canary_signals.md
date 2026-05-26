# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T18:37:21.834308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.882` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6986` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.3402` n `228`; crypto_major avg `-0.2735` n `8`; equity avg `-0.1283` n `67`; fx avg `0.0072` n `6`; index avg `0.0488` n `23`; metal avg `0.1054` n `18`; unknown avg `-0.3504` n `418`
- 1h: commodity avg `-0.1329` n `12`; crypto_alt avg `0.073` n `228`; crypto_major avg `0.1366` n `8`; equity avg `0.0243` n `67`; fx avg `0.0094` n `6`; index avg `0.1246` n `23`; metal avg `0.0945` n `18`; unknown avg `-0.4091` n `418`
- 4h: commodity avg `-0.2103` n `12`; crypto_alt avg `-2.1886` n `228`; crypto_major avg `-1.8197` n `8`; equity avg `-0.1211` n `67`; fx avg `0.0447` n `6`; index avg `0.0623` n `23`; metal avg `-0.3679` n `18`; unknown avg `1.6189` n `418`
- 24h: commodity avg `0.5485` n `12`; crypto_alt avg `-2.3989` n `228`; crypto_major avg `-1.7083` n `8`; equity avg `-0.3284` n `67`; fx avg `-0.1122` n `6`; index avg `0.4535` n `23`; metal avg `-1.3128` n `18`; unknown avg `-0.4184` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
