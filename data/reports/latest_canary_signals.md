# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T22:22:15.328121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2887` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3484` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0752` n `12`; crypto_alt avg `-0.196` n `228`; crypto_major avg `-0.1725` n `8`; equity avg `-0.057` n `67`; fx avg `0.0005` n `6`; index avg `-0.0012` n `23`; metal avg `0.004` n `18`; unknown avg `-0.0397` n `386`
- 1h: commodity avg `0.1651` n `12`; crypto_alt avg `-0.2858` n `228`; crypto_major avg `-0.1334` n `8`; equity avg `-0.0737` n `67`; fx avg `-0.0053` n `6`; index avg `-0.0568` n `23`; metal avg `0.0492` n `18`; unknown avg `-0.123` n `386`
- 4h: commodity avg `0.5692` n `12`; crypto_alt avg `-2.3559` n `228`; crypto_major avg `-1.7195` n `8`; equity avg `-0.9109` n `67`; fx avg `0.0247` n `6`; index avg `-0.3711` n `23`; metal avg `-0.2939` n `18`; unknown avg `1.2571` n `386`
- 24h: commodity avg `-0.5434` n `12`; crypto_alt avg `-2.8597` n `228`; crypto_major avg `-2.054` n `8`; equity avg `-1.2799` n `67`; fx avg `0.1553` n `6`; index avg `0.368` n `23`; metal avg `-1.0681` n `18`; unknown avg `-1.2041` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
