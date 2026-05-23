# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T08:52:18.010838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0129` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `0.4189` n `228`; crypto_major avg `0.1662` n `8`; equity avg `0.0574` n `67`; fx avg `0.0248` n `6`; index avg `-0.0144` n `23`; metal avg `0.0016` n `18`; unknown avg `0.8444` n `396`
- 1h: commodity avg `0.0714` n `12`; crypto_alt avg `0.3465` n `228`; crypto_major avg `0.3586` n `8`; equity avg `-0.1645` n `67`; fx avg `-0.0339` n `6`; index avg `0.0168` n `23`; metal avg `0.0336` n `18`; unknown avg `1.3804` n `386`
- 4h: commodity avg `0.0724` n `12`; crypto_alt avg `-2.0311` n `228`; crypto_major avg `-1.1889` n `8`; equity avg `-0.2863` n `67`; fx avg `-0.0246` n `6`; index avg `-0.176` n `23`; metal avg `0.0165` n `18`; unknown avg `0.7734` n `376`
- 24h: commodity avg `-0.4095` n `12`; crypto_alt avg `-5.742` n `228`; crypto_major avg `-3.9886` n `8`; equity avg `-2.0843` n `67`; fx avg `0.014` n `6`; index avg `-0.3609` n `23`; metal avg `-0.5269` n `18`; unknown avg `-1.2669` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
