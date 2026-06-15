# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T23:22:33.591367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1362` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1141` n `12`; crypto_alt avg `-0.0208` n `228`; crypto_major avg `-0.0973` n `8`; equity avg `-0.0112` n `77`; fx avg `-0.0287` n `6`; index avg `-0.0425` n `23`; metal avg `-0.0262` n `18`; unknown avg `-0.0852` n `687`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `-0.2609` n `228`; crypto_major avg `-0.4503` n `8`; equity avg `-0.021` n `77`; fx avg `0.0118` n `6`; index avg `-0.0423` n `23`; metal avg `0.1265` n `18`; unknown avg `0.4266` n `687`
- 4h: commodity avg `0.1195` n `12`; crypto_alt avg `-0.8228` n `228`; crypto_major avg `-1.2795` n `8`; equity avg `-0.0391` n `77`; fx avg `0.0145` n `6`; index avg `-0.1433` n `23`; metal avg `-0.2058` n `18`; unknown avg `0.6166` n `679`
- 24h: commodity avg `0.4908` n `12`; crypto_alt avg `0.9555` n `228`; crypto_major avg `2.3344` n `8`; equity avg `1.7325` n `76`; fx avg `-0.0743` n `6`; index avg `0.9099` n `23`; metal avg `0.4824` n `18`; unknown avg `1.9276` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
