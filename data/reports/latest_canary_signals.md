# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T08:07:15.316862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7626` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5948` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.036` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `-0.2377` n `228`; crypto_major avg `0.074` n `8`; equity avg `-0.3425` n `67`; fx avg `-0.0183` n `6`; index avg `0.0` n `23`; metal avg `-0.0181` n `18`; unknown avg `1.1913` n `386`
- 1h: commodity avg `-0.0592` n `12`; crypto_alt avg `-2.0947` n `228`; crypto_major avg `-1.1315` n `8`; equity avg `-0.4096` n `67`; fx avg `-0.0256` n `6`; index avg `-0.0955` n `23`; metal avg `-0.0852` n `18`; unknown avg `0.712` n `386`
- 4h: commodity avg `-0.1514` n `12`; crypto_alt avg `-2.8902` n `228`; crypto_major avg `-1.823` n `8`; equity avg `-0.5452` n `67`; fx avg `-0.009` n `6`; index avg `-0.2282` n `23`; metal avg `-0.0604` n `18`; unknown avg `0.2669` n `376`
- 24h: commodity avg `-0.4498` n `12`; crypto_alt avg `-6.3011` n `228`; crypto_major avg `-3.9729` n `8`; equity avg `-2.3796` n `67`; fx avg `0.0485` n `6`; index avg `-0.3126` n `23`; metal avg `-0.718` n `18`; unknown avg `-1.5843` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
